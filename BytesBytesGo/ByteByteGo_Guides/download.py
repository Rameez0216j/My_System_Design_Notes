import os
import requests
from bs4 import BeautifulSoup
import re



root_folder = "images"
os.makedirs(root_folder, exist_ok=True)


# Replace invalid characters with underscore or remove them
def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '', name)


# Function to get the anchor links from the initial page
def get_initial_links(base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the div containing the required links
    grid_div = soup.find(
        'div', {'class': 'grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3 md:gap-5'})
    if grid_div:
        # Extract all anchor tags
        spans = grid_div.find_all('span', {'class': 'relative font-semibold text-2xl line-clamp-2 transition-colors text-black'})
        anchors = grid_div.find_all('a', href=True)
        links = [anchor['href'] for anchor in anchors]
        names = [span.text for span in spans]
        return [links, names]
    return []


# Function to visit each link and get the anchor links from the specified div
def get_links_from_page(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the div containing the required anchor tags
    grid_div = soup.find(
        'div', {'class': 'grid grid-cols-1 gap-4 sm:grid-cols-2 sm:gap-5'})
    if grid_div:
        # Extract all anchor tags
        anchors = grid_div.find_all('a', href=True)
        links = [
            f"https://bytebytego.com{anchor['href']}" for anchor in anchors]
        return links
    return []

# Main function to loop through the initial links and get the links from each page


def main():
    base_url = "https://bytebytego.com/guides/"

    # Step 1: Get initial links
    initial_links = get_initial_links(base_url)[0]
    category_names = get_initial_links(base_url)[1]
    print(f"Found {len(initial_links)} links on the main page.")

    all_links = []
    link_by_category = []

    # Step 2: Visit each page and get the links
    for link in initial_links:
        # Construct the full URL for each page
        full_url = f"https://bytebytego.com{link}"
        print(f"Visiting {full_url}")

        page_links = get_links_from_page(full_url)
        print(f"Found {len(page_links)} links on {full_url}.")

        all_links.extend(page_links)
        link_by_category.append(page_links)

    # Print all the collected links
    print(f"\nTotal categories collected: {len(link_by_category)}")

    # dictionary to store categories with their links
    categories_links = {}
    for i, category in enumerate(category_names):
        categories_links[category] = link_by_category[i]

    # Change this below code only
    for category, links in categories_links.items():
        print(f"\nCategory: {category}")

        # Create category folder
        safe_category = sanitize_filename(category)
        category_path = os.path.join(root_folder, safe_category)
        os.makedirs(category_path, exist_ok=True)

        for idx, link in enumerate(links, start=1):
            print(f"Processing: {link}")
            try:
                response = requests.get(link)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, 'html.parser')

                # Find the target div and image
                div = soup.find('div', class_='prose prose-p:text-gray-600 prose-img:rounded-xl prose-img:w-full prose-h2:text-xl sm:prose-h2:text-2xl prose-h2:font-bold prose-h2:mb-2 prose-p:mb-4 sm:prose-p:mb-6 prose-p:leading-relaxed prose-base sm:prose-lg max-w-none')
                if not div:
                    print(f"No content div found in {link}")
                    continue

                img_tag = div.find("img")
                if not img_tag or not img_tag.get("src"):
                    print(f"No image tag found in {link}")
                    continue

                image_url = img_tag["src"]
                img_response = requests.get(image_url)
                img_response.raise_for_status()

                # Use category and index to form a filename
                filename = os.path.basename(image_url.split('?')[0])  # handles query strings if any
                file_path = os.path.join(category_path, filename)
                print(f"Saving image to {file_path}")

                with open(file_path, 'wb') as f:
                    f.write(img_response.content)

                print(f"Saved image to {file_path}")

            except Exception as e:
                print(f"Failed to process {link}: {e}")


if __name__ == "__main__":
    main()
